---
id: UDG@20.15.2@MMLCommand@LST PROTOCOLGROUP
type: MMLCommand
name: LST PROTOCOLGROUP（查询自定义协议组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PROTOCOLGROUP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 协议组
status: active
---

# LST PROTOCOLGROUP（查询自定义协议组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询自定义协议组；如果不指定可选参数，该命令将显示所有自定义协议组信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTOCOLGROUP]] · 自定义协议组（PROTOCOLGROUP）

## 使用实例

- 如果想要查询一条指定的自定义协议组“group1”，应该输入合法的数据，例如：
  ```
  LST PROTOCOLGROUP: PROTGROUPNAME="group1";
  ```
  ```

  RETCODE = 0  操作成功。

  自定义协议组信息
  ----------------
  协议组名称  =  group1
    协议名称  =  abc
  配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 如果想要查询所有的自定义协议组信息：
  ```
  LST PROTOCOLGROUP:;
  ```
  ```

  RETCODE = 0  操作成功。

  自定义协议组信息
  ----------------
  协议组名称     协议名称    配置域名称
   
  group1         abc     NULL
  group2         NULL    NULL
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询自定义协议组（LST-PROTOCOLGROUP）_86528709.md`
