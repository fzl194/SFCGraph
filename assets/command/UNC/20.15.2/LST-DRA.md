---
id: UNC@20.15.2@MMLCommand@LST DRA
type: MMLCommand
name: LST DRA（查询DRA）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRA
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
- DRA管理
- DRA信息
status: active
---

# LST DRA（查询DRA）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询DRA的基本信息。

可以查询一条指定的DRA信息，也可以查询所有的DRA。

## 注意事项

- 查询特定的DRA时，必须输入DRA主机名称。
- 如果不输入参数则是查询全部的DRA。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DRA的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRA]] · DRA（DRA）

## 使用实例

- 查询名称为“dra1”的DRA的信息：
  ```
  LST DRA:HOSTNAME="dra1";
  ```
  ```

  RETCODE = 0  操作成功

  DRA信息
  -------
   主机名  =  dra1
  VPN实例  =  vpn2
   DSCP值  =  46
    wal值  =  0
  DRA域名  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中所有的DRA信息：
  ```
  LST DRA:;
  ```
  ```

  RETCODE = 0  操作成功

  DRA信息
  -------
  主机名    VPN实例  DSCP值  wal值  DRA域名  

  dra1      vpn2     46      0      NULL     
  host1     vpn1     46      0      NULL     
  host2     vpn1     46      0      NULL     
  ocs1      NULL     46      0      NULL     
  ocs2      NULL     46      0      NULL     
  pcrfhost  vpn1     46      0      NULL     
  (结果个数 = 6)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DRA（LST-DRA）_09897294.md`
