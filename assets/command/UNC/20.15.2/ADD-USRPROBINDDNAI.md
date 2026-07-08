---
id: UNC@20.15.2@MMLCommand@ADD USRPROBINDDNAI
type: MMLCommand
name: ADD USRPROBINDDNAI（增加用户模板关联的DNAI）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: USRPROBINDDNAI
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板DNAI绑定
status: active
---

# ADD USRPROBINDDNAI（增加用户模板关联的DNAI）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户模板关联的DNAI。

当需要指定用户模板下发某边缘UPF时，可通过本命令绑定User Profile和边缘UPF的DNAI的对应关系来实现。

当一个用户模板绑定到某边缘UPF所对应的DNAI时，该用户模板就只下发给该边缘UPF。

## 注意事项

- 该命令执行后立即生效。

- 仅当指定用户模板中的Profile Range为LOCAL时，才可以绑定到边缘UPF对应的DNAI上。Profile Range为ALL的用户模板绑定DNAI无实际意义， SMF会将User Profile同时下发给中心和所有边缘UPF。Profile Range为CENTRAL时，该用户模板不能绑定到任何边缘UPF的DNAI上。

- 最多可输入10000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRPRONAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数通过ADD USERPROFILE命令配置生成。 |
| DNAI | 数据网络访问标识符 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识符。该参数的数据规划上需要和PNFDNAI命令中的“数据网络访问标识”参数保持一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRPROBINDDNAI]] · 用户模板关联的DNAI（USRPROBINDDNAI）

## 使用实例

如果要增加用户模板关联的DNAI，则使用此命令。

```
ADD USRPROBINDDNAI: USRPRONAME="userprofile1", DNAI="huawei1.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-USRPROBINDDNAI.md`
