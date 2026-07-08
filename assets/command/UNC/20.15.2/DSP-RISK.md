---
id: UNC@20.15.2@MMLCommand@DSP RISK
type: MMLCommand
name: DSP RISK（显示系统风险）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RISK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 安全风险
status: active
---

# DSP RISK（显示系统风险）

## 功能

该命令用于显示系统风险。可根据风险提示中修复方法消除风险。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RISKLEVEL | 风险等级 | 可选必选说明：可选参数<br>参数含义：风险等级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- high：高风险。<br>- medium：中风险。<br>- low：低风险。<br>默认值：无 |
| FEATURENAME | 特性名称 | 可选必选说明：可选参数<br>参数含义：特性名称。目前支持的特性范围为：CONFIGURATION-MANAGEMENT（配置管理）、DSA（SSH公钥算法DSA）、ECC（SSH公钥算法ECC）、INFO（日志管理）、NTP（时间管理）、RSA（SSH公钥算法RSA）、SSH_CLIENT（接入配置管理SH客户端）、GRSA（SSH公钥算法GRSA）、SSL（接入配置管理SSL）、VTY（接入配置管理VTY）、TTY（接入配置管理TTY）。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RISK]] · 系统风险（RISK）

## 使用实例

- 显示所有风险：
  ```
  DSP RISK:;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  风险等级    特性名称      风险提示                                                         修复方法

  高          SSH_CLIENT    SSH客户端存在不安全的摘要算法（sha1_96，sha2_256_96）            建议关闭不安全的摘要算法
  高          VTY           闲置切断时间为零，因此会话永远不会超时断连                       配置闲置切断时间为非零值
  (结果个数 = 2)
  ---    END
  ```
- 显示SSH_CLIENT特性的风险：
  ```
  DSP RISK:FEATURENAME="SSH_CLIENT";
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  风险等级  =  高
  特性名称  =  SSH_CLIENT
  风险提示  =  SSH客户端存在不安全的摘要算法（sha1_96，sha2_256_96）
  修复方法  =  建议关闭不安全的摘要算法
  (结果个数 = 1)
  ---    END
  ```
- 显示高级别风险：
  ```
  DSP RISK:RISKLEVEL=high;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  风险等级    特性名称      风险提示                                                         修复方法

  高          SSH_CLIENT    SSH客户端存在不安全的摘要算法（sha1_96，sha2_256_96）            建议关闭不安全的摘要算法
  高          VTY           闲置切断时间为零，因此会话永远不会超时断连                       配置闲置切断时间为非零值
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RISK.md`
