---
id: UNC@20.15.2@MMLCommand@DSP SECTIONUSAGE
type: MMLCommand
name: DSP SECTIONUSAGE（显示地址段使用信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SECTIONUSAGE
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址段使用信息
status: active
---

# DSP SECTIONUSAGE（显示地址段使用信息）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于显示地址段使用信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定已配的本地地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定已配的地址段编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD SECTION命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECTIONUSAGE]] · 地址段使用信息（SECTIONUSAGE）

## 使用实例

显示地址池名称为testpool的0号地址段的使用率信息： DSP SECTIONUSAGE: POOLNAME="testpool", SECTIONNUM=0;

```
%%DSP SECTIONUSAGE: POOLNAME="testpool", SECTIONNUM=0;%%
RETCODE = 0  操作成功

结果如下
-------------------------
   地址池名称  =  testpool
     地址段号  =  0
     地址总数  =  32
   地址使用数  =  1
   无效地址数  =  0
地址使用率(%)  =  3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示地址段使用信息（DSP-SECTIONUSAGE）_20028093.md`
