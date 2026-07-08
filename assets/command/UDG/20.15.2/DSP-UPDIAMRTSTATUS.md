---
id: UDG@20.15.2@MMLCommand@DSP UPDIAMRTSTATUS
type: MMLCommand
name: DSP UPDIAMRTSTATUS（显示Diameter Route状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPDIAMRTSTATUS
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- 路由管理
- 路由状态
status: active
---

# DSP UPDIAMRTSTATUS（显示Diameter Route状态）

## 功能

**适用NF：UPF**

此命令用来查询Diameter路由的状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALM | Diameter域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter应用的域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter协议中的应用类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMRTSTATUS]] · Diameter Route状态（UPDIAMRTSTATUS）

## 使用实例

- 查询Diameter realm为"swm-realm"的Diameter Route信息：
  ```
  DSP UPDIAMRTSTATUS: REALM="swm-realm-realm",APPLICATION=SWM;
  ```
  ```

  RETCODE = 0  操作成功。
  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称       状态    
  swm-realm       Swm             updiam-pod-0  Normal  
  swm-realm       Swm             updiam-pod-0  Abnormal
  (结果个数 = 2)
  ```
- 查询全部Diameter Route信息：
  ```
  DSP UPDIAMRTSTATUS:;
  ```
  ```

  RETCODE = 0  操作成功。
  Diameter路由状态
  ----------------
  Diameter域名    Diameter应用    POD名称       状态    
  swm-realm       Swm             updiam-pod-0  Normal  
  swm-realm       Swm             updiam-pod-0  Abnormal
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UPDIAMRTSTATUS.md`
