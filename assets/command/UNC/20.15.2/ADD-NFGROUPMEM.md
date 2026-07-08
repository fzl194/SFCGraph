---
id: UNC@20.15.2@MMLCommand@ADD NFGROUPMEM
type: MMLCommand
name: ADD NFGROUPMEM（增加NF组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFGROUPMEM
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例组信息管理
status: active
---

# ADD NFGROUPMEM（增加NF组成员）

## 功能

**适用NF：NRF**

该命令用于在NRF上为NF实例组添加NF实例成员。

“NF组标识”添加多个“NF实例标识”时，需要每个NF实例对外提供相同的业务功能。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：必选参数<br>参数含义：该参数表示在NRF上配置的NF实例组标识，输入该参数时，可通过LST NFGROUP命令获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数表示在NRF上配置的NF实例组成员。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFNAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组下的成员NF实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF组成员（NFGROUPMEM）](configobject/UNC/20.15.2/NFGROUPMEM.md)

## 使用实例

- 运营商想在NRF上新增NF标识为nfgroup001，NF类型为CHF，组描述为nfdescription001的实例组，执行此命令。
  ```
  ADD NFGROUP: NFGROUPID="nfgroup001", NFTYPE=CHF, GROUPDESC="nfdescription001";
  ```
- 运营商想在NRF上添加组标识为nfgroup001，实例标识为Instanceid01，实例名称为superom11-v6的NF实例组成员，执行此命令。
  ```
  ADD NFGROUPMEM: NFGROUPID="nfgroup001", NFINSTANCEID="Instanceid01", NFNAME="superom11-v6";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF组成员（ADD-NFGROUPMEM）_09652338.md`
