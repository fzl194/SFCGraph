# 显示ResourceBox重建历史记录（DSP RSCBOXHEALREC）

- [命令功能](#ZH-CN_MMLREF_0000001400601670__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001400601670__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001400601670__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001400601670__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001400601670__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001400601670)

该命令用于查询ResourceBox重建历史记录。

## [注意事项](#ZH-CN_MMLREF_0000001400601670)

该命令只适用于裸机容器云场景。

#### [操作用户权限](#ZH-CN_MMLREF_0000001400601670)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001400601670)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSCBOXNAME | ResourceBox名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示重建的ResourceBox名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。如果不输入该输出，则查询系统内所有ResourceBox的重建记录。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001400601670)

查询ResourceBox重建历史记录:

```
DSP RSCBOXHEALREC:;
RETCODE = 0  操作成功

结果如下
--------
ResourceBox名称                堆栈ID                               重建时间            序号  ResourceBoxID
vsm-super-pod-54ddc977b9-4g42g 524c409a-bc3b-11ea-a186-025565660064 2020-07-09 09:08:03 1     c2208db2-bc3b-11ea-9d1b-fa163eb94edd 
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001400601670)

| 输出项名称 | 输出项解释 |
| --- | --- |
| ResourceBox名称 | 该参数用于显示重建的ResourceBox名称。 |
| 堆栈ID | 该参数用于显示ResourceBox所属的堆栈ID。 |
| 重建时间 | 该参数用于显示ResourceBox重建的时间。 |
| 序号 | 该参数用于记录重建ResourceBox的序号。 |
| ResourceBoxID | 该参数用于显示ResourceBoxID。 |
