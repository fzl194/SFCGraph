# 显示预占RU资源（DSP PREOCCUPYRES）

- [命令功能](#ZH-CN_CONCEPT_0251174357__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174357__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174357__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174357__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174357__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174357__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0251174357__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174357)

**适用NF：NCG**

该命令用于显示预占的RU资源。

#### [注意事项](#ZH-CN_CONCEPT_0251174357)

该命令需等待 [**ACT PREOCCUPYRES**](预占RU资源（ACT PREOCCUPYRES）_51174356.md) 命令执行成功30秒后执行。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174357)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174357)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174357)

无。

#### [使用实例](#ZH-CN_CONCEPT_0251174357)

显示预占的RU资源：

```
DSP PREOCCUPYRES:;
```

```
RETCODE = 0  操作成功。
结果如下:
---------
         RU类型  =  CG_SP_RU
       预占数量  =  2
RU所在的HOST ID  =  8BF6E523-1800-9391-B211-D21D0C3EDC2B;8BF6E523-1800-ECBF-B211-D21D26ABAE2C
   命令返回结果  =  成功
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0251174357)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU类型 | 用于指定预占RU的类型。 |
| 预占数量 | 用于指定预占RU的个数。 |
| RU所在的HOST ID | 用于指定预占RU所在的HostId。 |
| 命令返回结果 | 用于指定预占RU命令的返回结果。 |
