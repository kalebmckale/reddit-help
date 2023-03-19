from os import listdir, makedirs, mkdir
from os.path import exists
from subprocess import run, PIPE, CalledProcessError
import multiprocessing

base_folders = ["enderal - forgotten stories.esm", "skyrim.esm"]
source_file_names = []


def create_lips_for_voice_type(plugin_name: str, voice_type: str) -> None:
    base = f"{plugin_name}/{voice_type}"
    log_dir = f"logs/{base}"
    resampled_dir = f"resamples/{base}"

    if not exists("logs"):
        mkdir("logs")

    makedirs(log_dir, exist_ok=True)
    makedirs(resampled_dir, exist_ok=True)

    with open(f"{log_dir}/log.txt", "w") as log:
        pass

    for file in [i for i in listdir(base) if i.endswith(".wav")]:
        the_Path = f"{base}/{file}"[:-4:]  # exclude file type
        text = (
            "Numa numa je. Numa numa jej."
        )  # testing purpouses, next time I will take data from XML export of xTranslator
        command = f"""FaceFXWrapper Skyrim USEnglish FonixData.cdf "{the_Path}.wav" "{resampled_dir}/{file}" "{the_Path}.lip" "{text}" """
        try:
            proc = run(command, check=True, stdout=PIPE, text=True)
        except CalledProcessError:
            with open(f"{log_dir}/log.txt", "a") as log:
                log.write(f"{proc.stdout}\n")


if __name__ == "__main__":
    jobs = []
    params_list = []
    for base_f in base_folders[1::]:
        voice_types_list = listdir(base_f)
        for vt in voice_types_list[1::]:
            params_list.append((base_f, vt))

    with multiprocessing.Pool(60) as pool:
        job = pool.starmap(create_lips_for_voice_type, params_list)
        jobs.append(job)
        pool.terminate()
