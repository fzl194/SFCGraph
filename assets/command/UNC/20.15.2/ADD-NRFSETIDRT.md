---
id: UNC@20.15.2@MMLCommand@ADD NRFSETIDRT
type: MMLCommand
name: ADD NRFSETIDRT（增加NF Set ID最长匹配后缀转发路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFSETIDRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- NF Set ID最长后缀匹配转发路由管理
status: active
---

# ADD NRFSETIDRT（增加NF Set ID最长匹配后缀转发路由）

## 功能

**适用NF：NRF**

该命令用于增加基于NF Set ID的最长匹配后缀的转发路由。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFSETIDSUFFIX | NF Set ID后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF Set ID后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、下划线（_）和点（.）组成，大小写不敏感，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于NF Set ID的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSETIDRT]] · NF Set ID最长匹配后缀转发路由（NRFSETIDRT）

## 使用实例

增加一条NF Set ID后缀为32123ASDF，归属NRF组名称为azh0701的最长匹配后缀的转发路由配置，执行如下命令：

```
ADD NRFSETIDRT: NFSETIDSUFFIX="32123ASDF", NEXTNRFGRPNAME="azh0701";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF-Set-ID最长匹配后缀转发路由（ADD-NRFSETIDRT）_72598769.md`
