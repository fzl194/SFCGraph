---
id: UDG@20.15.2@MMLCommand@DSP TUNNELPOLICY
type: MMLCommand
name: DSP TUNNELPOLICY（显示隧道策略信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TUNNELPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- VPN隧道管理
- 隧道策略
status: active
---

# DSP TUNNELPOLICY（显示隧道策略信息）

## 功能

该命令用于显示隧道策略信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISPOLICYCOUNT | 是否仅查询策略个数 | 可选必选说明：必选参数<br>参数含义：该参数用于表示是否仅查询策略个数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：否。<br>- TRUE：是。<br>默认值：无 |
| TNLPOLICYNAME | 隧道策略名字 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISPOLICYCOUNT”配置为“FALSE”时为可选参数。<br>参数含义：该参数用于表示隧道策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TUNNELPOLICY]] · 隧道策略（TUNNELPOLICY）

## 使用实例

- 显示隧道策略信息：
  ```
  DSP TUNNELPOLICY:ISPOLICYCOUNT=FALSE;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
    隧道策略名字  =  tp
  隧道类型序列号  =  GRE LSP
      负载分担数  =  50
  (结果个数 = 1)
  ---    END
  ```
- 显示隧道策略信息，仅查询策略个数：
  ```
  DSP TUNNELPOLICY:ISPOLICYCOUNT=TRUE;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
    策略总数  =  1
  选择策略数  =  1
  无效策略数  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-TUNNELPOLICY.md`
