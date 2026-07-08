# 查询APN ATSSS功能（LST APNATSSSFUNC）

- [命令功能](#ZH-CN_MMLREF_0296242064__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242064__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242064__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242064__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242064__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242064)

**适用NF：SMF**

该命令用于查询指定APN ATSSS功能参数。

## [注意事项](#ZH-CN_MMLREF_0296242064)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242064)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242064)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0296242064)

查询指定APN下的ATSSS功能开关配置：

```
LST APNATSSSFUNC: APN="huawei.com";
%%LST APNATSSSFUNC: APN="huawei.com";%%
RETCODE = 0  操作成功

APN ATSSS功能参数
----------------------------
      APN名称  =  huawei.com
ATSSS功能开关  =  disable
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242064)

| 输出项名称 | 输出项解释 |
| --- | --- |
| APN名称 | 该参数用于指定APN实例名。 |
| ATSSS功能开关 | 该参数用于指定是否使能ATSSS功能。 |
