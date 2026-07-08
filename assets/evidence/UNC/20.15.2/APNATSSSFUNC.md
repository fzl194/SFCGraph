# 设置APN ATSSS功能（SET APNATSSSFUNC）

- [命令功能](#ZH-CN_MMLREF_0296243070__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296243070__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296243070__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296243070__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0296243070)

**适用NF：SMF**

该命令用于设置APN的ATSSS功能参数。

## [注意事项](#ZH-CN_MMLREF_0296243070)

- 该命令执行后只对新激活用户生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：ATSSSFUNCSWITCH：DISABLE。

#### [操作用户权限](#ZH-CN_MMLREF_0296243070)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0296243070)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无。<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| ATSSSFUNCSWITCH | ATSSS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使能ATSSS功能。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：不使能功能<br>- “ENABLE（使能）”：打开ATSSS功能开关<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNATSSSFUNC查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0296243070)

使能指定APN的ATSSS功能：

```
SET APNATSSSFUNC: APN="huawei.com", ATSSSFUNCSWITCH=ENABLE;
%%SET APNATSSSFUNC: APN="huawei.com", ATSSSFUNCSWITCH=ENABLE;%%
RETCODE = 0  操作成功

---    END
```
