# 查询License配置项开关（LST LICENSESWITCH）

- [命令功能](#ZH-CN_MMLREF_0209587900__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209587900__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209587900__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209587900__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209587900__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209587900)

该命令用于查看License项的名称以及License项的开关配置情况。

> **说明**
> - 该命令执行后立即生效。
> - 当License文件未激活时，查询结果为空，激活后只能查询已购买且支持配置开关的License项。

#### [操作用户权限](#ZH-CN_MMLREF_0209587900)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209587900)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LICITEM | License项 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要开通的License项。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209587900)

查询License项“LKV2INLIAM01”的配置开关：

```
%%LST LICENSESWITCH: LICITEM="LKV2INLIAM01";%%
RETCODE = 0  操作成功

操作结果如下
------------
  License项  =  LKV2INLIAM01
License名称  =  IPv6 Networking on Logic Interface-UAM
       开关  =  开
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209587900)

| 输出项名称 | 输出项解释 |
| --- | --- |
| License项 | 该参数用于指定需要开通的License项。 |
| License名称 | 该参数用于表示License项的名称。 |
| 开关 | 该参数用于表示License项的配置开关是否已经打开。 |
