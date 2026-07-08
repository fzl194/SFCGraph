---
id: UDG@20.15.2@MMLCommand@DSP UPDRASTATUS
type: MMLCommand
name: DSP UPDRASTATUS（显示DRA状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPDRASTATUS
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- DRA管理
- DRA状态
status: active
---

# DSP UPDRASTATUS（显示DRA状态）

## 功能

**适用NF：UPF**

此命令用于查询所有DRA或者指定DRA的链接状态。

## 注意事项

- 未配置Diameter链路组的DRA不显示。
- 如果显示“No Link”记录，则说明此DRA未配置Diameter链路。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | DRA主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示查询DRA的主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDRASTATUS]] · DRA状态（UPDRASTATUS）

## 使用实例

- 查询指定主机名的DRA的状态信息：
  ```
  DSP UPDRASTATUS:HOSTNAME="dra1";
  ```
  ```

  RETCODE = 0  操作成功。
  DRA状态
  -------
   DRA主机名  =  dra1
     POD名称  =  updiam-pod-0
    本端地址  =  10.10.10.11:13450
  本端子地址  =  -
    对端地址  =  172.16.0.1:3868
    正常链路  =  -
    异常链路  =  swm
      无链路  =  -
  本端主机名  =  swmlocal
  (结果个数 = 1)
  ---    END
  ```
- 查询所有DRA的状态信息：
  ```
  DSP UPDRASTATUS:;
  ```
  ```

  RETCODE = 0  操作成功。
  DRA状态
  -------
  DRA主机名    POD名称       本端地址             本端子地址       对端地址            正常链路    异常链路    无链路     本端主机名          
  dra1         updiam-pod-0  10.10.10.11:13450    -                172.16.0.1:3868     -           swm         -          swmlocal  
  drasctp      updiam-pod-0  10.10.10.11:13400    -                dra_sctp            -           swm         -          swmlocal  
  (Number of results = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UPDRASTATUS.md`
