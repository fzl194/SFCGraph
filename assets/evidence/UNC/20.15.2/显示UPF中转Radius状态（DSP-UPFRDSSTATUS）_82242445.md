# 显示UPF中转Radius状态（DSP UPFRDSSTATUS）

- [命令功能](#ZH-CN_MMLREF_0000001182242445__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001182242445__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001182242445__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001182242445__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001182242445__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001182242445)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查看UPF中转Radius状态。当前最多支持显示100条记录。

## [注意事项](#ZH-CN_MMLREF_0000001182242445)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001182242445)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001182242445)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AAATYPE | AAA类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定AAA类型。<br>数据来源：本端规划<br>取值范围：<br>- “AUTHENTICATION（AAA鉴权）”：表示AAA鉴权。<br>- “ACCOUNTING（AAA计费）”：表示AAA计费。<br>默认值：无<br>配置原则：无 |
| UPFINSTANCE | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001182242445)

显示UPF中转Radius状态。

```
%%DSP UPFRDSSTATUS:;%%
RETCODE = 0  操作成功

结果如下
------------------------
AAA类型        UPF实例名称      UPF中转Radius状态

AAA鉴权        upf_instance_1   异常
AAA计费        upf_instance_2   异常
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001182242445)

| 输出项名称 | 输出项解释 |
| --- | --- |
| AAA类型 | 该参数用于指定AAA类型。<br>取值说明：<br>- “AUTHENTICATION（AAA鉴权）”：表示AAA鉴权。<br>- “ACCOUNTING（AAA计费）”：表示AAA计费。 |
| UPF实例名称 | 该参数用于指定UPF实例名称。 |
| UPF中转Radius状态 | 该参数用于指定UPF中转Radius状态。<br>取值说明：<br>- “ABNORMAL（异常）”：表示状态异常。<br>- “NORMAL（正常）”：表示状态正常。 |
