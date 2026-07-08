---
id: UDG@20.15.2@MMLCommand@LST SRVCHAIN
type: MMLCommand
name: LST SRVCHAIN（查询业务链）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVCHAIN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 业务链配置
status: active
---

# LST SRVCHAIN（查询业务链）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询业务链配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVCHAINNAME | 业务链名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务链名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [业务链（SRVCHAIN）](configobject/UDG/20.15.2/SRVCHAIN.md)

## 使用实例

- 如果运营商想要查询业务链名称为TestSrvChain的业务链配置。命令如下：
  ```
  LST SRVCHAIN: SRVCHAINNAME="TestSrvChain";
  ```
  ```

  RETCODE = 0  操作成功。

  业务链信息
  ----------
    业务链名称  =  testsrvchain
  上行业务链ID  =  101
  下行业务链ID  =  201
  (结果个数 = 1)
  ---    END
  ```
- 如果运营商想要查询所有业务链配置。命令如下：
  ```
  LST SRVCHAIN:;
  ```
  ```

  RETCODE = 0  操作成功。

  业务链信息
  ----------
  业务链名称      上行业务链ID    下行业务链ID

  testanother     102             202         
  testsrvchain    101             201         
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务链（LST-SRVCHAIN）_41687095.md`
