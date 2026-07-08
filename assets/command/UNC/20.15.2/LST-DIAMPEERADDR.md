---
id: UNC@20.15.2@MMLCommand@LST DIAMPEERADDR
type: MMLCommand
name: LST DIAMPEERADDR（查询Diameter对端地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMPEERADDR
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- 服务器地址
status: active
---

# LST DIAMPEERADDR（查询Diameter对端地址）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter对端地址的信息。

可以查询指定主机的地址信息，也可以查询所有的地址信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址信息所属的Diameter主机名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 查询特定的主机的地址信息时，必须输入主机名称。<br>- 如果不输入参数则是查询所有Diameter主机的地址信息。 |

## 操作的配置对象

- [Diameter对端地址（DIAMPEERADDR）](configobject/UNC/20.15.2/DIAMPEERADDR.md)

## 使用实例

- 查询Diameter主机名为“ocs1”的Diameter对端地址信息：
  ```
  LST DIAMPEERADDR: HOSTNAME="ocs1";
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter对端地址信息
  --------------------
      主机名称  =  ocs1
      地址类型  =  IPv4
        IP地址  =  10.10.10.10
        端口号  =  3868
  SCTP端点名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询系统中所有的Diameter对端地址信息：
  ```
  LST DIAMPEERADDR:;
  ```
  ```

  RETCODE = 0  操作成功。

  Diameter对端地址信息
  --------------------
  主机名称              地址类型    IP地址          端口号    SCTP端点名称
      
  ocs1                  IPv4        10.10.10.10     3868      NULL   
  ocs2                  SCTP        NULL            0         end1       
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter对端地址（LST-DIAMPEERADDR）_09897259.md`
