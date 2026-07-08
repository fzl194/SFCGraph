# 显示vprobeexec-pod的磁盘空间大小（DSP VPROBEDISKSIZE）

- [命令功能](#ZH-CN_MMLREF_0000001388723156__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001388723156__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001388723156__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001388723156__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001388723156__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001388723156)

此命令用于查询vprobeexec-pod的磁盘空间大小。

## [注意事项](#ZH-CN_MMLREF_0000001388723156)

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

#### [操作用户权限](#ZH-CN_MMLREF_0000001388723156)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001388723156)

无

## [使用实例](#ZH-CN_MMLREF_0000001388723156)

查询vprobeexec-pod的磁盘空间：

```
%%DSP VPROBEDISKSIZE:;%%
RETCODE = 0  操作成功

结果如下
--------
vProbe Pod ID     vProbe可用磁盘总空间(GB)  

vprobeexec-pod-0  64                        
vprobeexec-pod-1  64                        
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001388723156)

| 输出项名称 | 输出项解释 |
| --- | --- |
| vProbe Pod ID | 该参数用于表示vProbe服务的Pod ID。 |
| vProbe可用磁盘总空间(GB) | 该参数用于表示vProbe服务当前可用磁盘总空间，单位为GB。 |
