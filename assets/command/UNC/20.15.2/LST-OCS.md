---
id: UNC@20.15.2@MMLCommand@LST OCS
type: MMLCommand
name: LST OCS（查询OCS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OCS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Server
status: active
---

# LST OCS（查询OCS）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询OCS的基本信息。可以查询一条指定的OCS的信息，也可以查询所有的OCS的信息。

## 注意事项

- 查询指定的OCS时，必须输入OCS主机名称。
- 如果不输入OCS主机名，则查询全部OCS信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSHOSTNAME | Ocs主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：如果输入则查询特定的OCS，如果不输入则查询系统中所有的OCS信息。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OCS]] · OCS（OCS）

## 使用实例

- 查询系统中名称为“ocs1”的OCS的信息：
  ```
  LST OCS:OCSHOSTNAME="ocs1";
  ```
  ```

  RETCODE = 0  操作成功。

  ocs-info配置信息
  ----------------
  Ocs主机名称  =  ocs1
      Ocs域名  =  www.huawei.com
      VPN实例  =  vpn1
       DSCP值  =  255
        wal值  =  0
  (结果个数 = 1)
  ---    END
  ```
- 查询系统中所有的OCS信息：
  ```
  LST OCS:;
  ```
  ```

  RETCODE = 0  操作成功。

  ocs-info配置信息
  ----------------
  Ocs主机名称    Ocs域名            VPN实例    DSCP值    wal值

  ocs1           www.huawei.com    vpn1       255       0    
  ocs2           www.huawei.com    NULL       255       0    
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OCS.md`
