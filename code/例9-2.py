def fileCopy(src, dst, srcEncoding, dstEncoding):
    with open(src, 'r', encoding=srcEncoding) as srcfp:
        with open(dst, 'w', encoding=dstEncoding) as dstfp:
            dstfp.write(srcfp.read())

fileCopy('sample.txt', 'sample_new.txt', 'cp936', 'utf8')
