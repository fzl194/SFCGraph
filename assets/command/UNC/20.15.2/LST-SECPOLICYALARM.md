---
id: UNC@20.15.2@MMLCommand@LST SECPOLICYALARM
type: MMLCommand
name: LST SECPOLICYALARM（查询安全策略告警配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SECPOLICYALARM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略告警
status: active
---

# LST SECPOLICYALARM（查询安全策略告警配置）

## 功能

该命令用来查询上送CPU报文产生告警参数的配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：安全策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：可选参数<br>参数含义：策略类型，如应用层联动、TCP/IP防攻击、黑白名单等。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- TotalPkt：所有报文。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- Index：索引策略。<br>- UserFlow：用户自定义流策略。<br>- APP：APP应用策略。<br>- Urpf：URPF策略。<br>- WhiteListV6：IPv6白名单。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：可选参数<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICYALARM]] · 安全策略告警配置（SECPOLICYALARM）

## 使用实例

- 查询上送CPU报文产生告警参数的配置：
  ```
  LST SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
            安全策略类型  =  白名单策略
            安全策略编号  =  1
        安全策略类型编号  =  0
            安全告警使能  =  TRUE
            安全告警阈值  =  1
  安全告警时间间隔（秒）  =  60
  (结果个数 = 1)
  ---    END
  ```
- 查询指定条件的上送CPU报文产生告警参数的配置：
  ```
  LST SECPOLICYALARM:SECPOLICYID=1,SECPOLICYTYPE=WhiteList,SECPOLICYTYPEID=0;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  --------
           安全策略类型  =  白名单策略
           安全策略编号  =  1
       安全策略类型编号  =  0
           安全告警使能  =  TRUE
           安全告警阈值  =  1
  安全告警时间间隔（秒） =  60
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询安全策略告警配置（LST-SECPOLICYALARM）_00841601.md`
