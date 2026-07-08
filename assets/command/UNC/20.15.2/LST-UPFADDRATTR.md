---
id: UNC@20.15.2@MMLCommand@LST UPFADDRATTR
type: MMLCommand
name: LST UPFADDRATTR（查询UPF地址属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFADDRATTR
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- UPF粒度PFCP路径参数管理
status: active
---

# LST UPFADDRATTR（查询UPF地址属性）

## 功能

**适用NF：SMF**

该命令用于查询UPF地址属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“NFINSTANCEID”参数取值相同。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFADDRATTR]] · UPF地址属性（UPFADDRATTR）

## 使用实例

- 以下命令用于查询所有UPF地址属性
  ```
  LST UPFADDRATTR:;
  ```
- 以下命令用于查询实例名称为upf1的UPF地址属性
  ```
  LST UPFADDRATTR: NFINSTANCEID="upf1";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPFADDRATTR.md`
