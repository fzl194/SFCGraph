# 查询UPF和DNS关联的UPF组的绑定关系（LST UEDNSUPFBINDGRP）

- [命令功能](#ZH-CN_MMLREF_0296242511__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242511__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242511__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242511__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242511__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242511)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询UPF和DNS关联的UPF组的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0296242511)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242511)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242511)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD UEDNSUPGROUP命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0296242511)

查询UPF和UPF组的绑定关系：

```
LST UEDNSUPFBINDGRP: UPFGRPNAME="upfgrp1";
RETCODE = 0  操作成功

结果如下
--------
  UPF组名称  =  upfgrp1
UPF实例名称  =  upf_instance_1
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242511)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UPF组名称 | 该参数用于指定UPF组的名称。 |
| UPF实例标识 | 该参数用于指定UPF实例名称。 |
