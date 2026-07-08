---
id: UDG@20.15.2@MMLCommand@ADD FILTERGROUP
type: MMLCommand
name: ADD FILTERGROUP（增加过滤器组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: FILTERGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 8000
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 过滤器组
status: active
---

# ADD FILTERGROUP（增加过滤器组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加过滤器组，添加过滤器到过滤器组。

## 注意事项

- 该命令执行后需要等待执行SET REFRESHSRV命令（REFRESHTYPE参数设置为USERPROFILE或ALL）刷新后生效。
- 该命令最大记录数为8000。当配置记录数大于规格的90%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格90%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 单个FilterGroup可以配置5000个Filter。
- 最多支持100000条Filter和FilterGroup的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERGRPNAME | 过滤器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FILTERNAME | 过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [过滤器组（FILTERGROUP）](configobject/UDG/20.15.2/FILTERGROUP.md)

## 使用实例

- 如果要添加一个名称为group1的过滤器组，执行如下命令：
  ```
  ADD FILTERGROUP: FILTERGRPNAME="group1";
  ```
- 如果要添加名称为filter1的过滤器，到过滤器组group1中，执行如下命令：
  ```
  ADD FILTERGROUP: FILTERGRPNAME="group1", FILTERNAME="filter1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加过滤器组（ADD-FILTERGROUP）_95089582.md`
