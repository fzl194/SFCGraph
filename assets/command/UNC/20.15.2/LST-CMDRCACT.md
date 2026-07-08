---
id: UNC@20.15.2@MMLCommand@LST CMDRCACT
type: MMLCommand
name: LST CMDRCACT（查询命令层异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CMDRCACT
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
- 信用控制
- 命令层返回码控制
status: active
---

# LST CMDRCACT（查询命令层异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询命令层异常返回码的处理动作配置。

## 注意事项

仅输入在线计费模板名称参数，查询结果为该在线计费模板下的所有命令层异常返回码处理动作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | 在线计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| CMDRC | 命令层异常返回码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定命令层异常返回码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CMDRCACT]] · 命令层异常返回码处理动作（CMDRCACT）

## 使用实例

- 查询全局在线计费模板的所有命令层异常返回码处理动作：
  ```
  LST CMDRCACT:DCCTMPLTNAME="global";
  ```
  ```

  RETCODE = 0  操作成功

  命令层异常返回码动作
  --------------------
                在线计费模板名称  =  global
                命令层异常返回码  =  5012
        命令层异常返回码处理动作  =  重定向
         命令层去活原因值GtpV0-1  =  0
           命令层去活原因值GtpV2  =  0
  命令层重定向处理重定向IPv4地址  =  192.168.10.16
  命令层重定向处理重定向IPv6地址  =  NULL
           CCA Holding Timer开关  =  关闭
              命令层重新激活请求  =  禁止
  (结果个数 = 1)
  --- END
  ```
- 查询全局在线计费模板中命令层异常返回码为5012的处理动作：
  ```
  LST CMDRCACT: DCCTMPLTNAME="global",CMDRC="5012";
  ```
  ```
  %%
  RETCODE = 0  操作成功

  命令层异常返回码动作
  --------------------
                在线计费模板名称  =  global
                命令层异常返回码  =  5012
        命令层异常返回码处理动作  =  重定向
         命令层去活原因值GtpV0-1  =  0
           命令层去活原因值GtpV2  =  0
  命令层重定向处理重定向IPv4地址  =  192.168.10.16
  命令层重定向处理重定向IPv6地址  =  NULL
           CCA Holding Timer开关  =  关闭
              命令层重新激活请求  =  禁止
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CMDRCACT.md`
