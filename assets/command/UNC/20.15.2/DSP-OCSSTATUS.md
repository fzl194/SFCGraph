---
id: UNC@20.15.2@MMLCommand@DSP OCSSTATUS
type: MMLCommand
name: DSP OCSSTATUS（查询OCS状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OCSSTATUS
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
- OCS状态
status: active
---

# DSP OCSSTATUS（查询OCS状态）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询OCS连接状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | OCS主机名 | 可选必选说明：可选参数<br>参数含义：OCS主机名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OCSSTATUS]] · OCS状态（OCSSTATUS）

## 使用实例

- 查询指定OCS服务器的连接状态：
  ```
  DSP OCSSTATUS:HOSTNAME="ocs-host-name";
  ```
  ```

  RETCODE = 0  操作成功。

  OCS状态
  -------
   OCS主机名  =  ocs-host-name
     POD名称  =  uncpod-0131-30-0-197
    本端地址  =  10.1.1.1:10200
  本端子地址  =  -
    对端地址  =  10.2.2.2:3868
   Gy Status  =  正常
  本端主机名  =  gylocal
  (结果个数 = 1)
  ---    END
  ```
- 查询所有OCS服务器的连接状态：
  ```
  DSP OCSSTATUS:;
  ```
  ```

  OCS状态
  -------
  OCS主机名      POD名称               本端地址           本端子地址  对端地址       Gy Status  本端主机名
                                                                                                                            
  ocs-host-name  uncpod-0131-30-0-197  192.168.0.1:10240  -           10.2.2.2:3868  异常       gylocal     
  ocs-name       uncpod-0131-30-0-197  192.168.0.1:10200  -           10.3.3.3:3868  正常       gylocal     
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OCSSTATUS.md`
