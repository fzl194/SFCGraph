---
id: UDG@20.15.2@MMLCommand@DSP LOGBUFFER
type: MMLCommand
name: DSP LOGBUFFER（显示Logbuffer中的数据）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LOGBUFFER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 日志管理
status: active
---

# DSP LOGBUFFER（显示Logbuffer中的数据）

## 功能

该命令用于显示日志缓冲区内容，包括操作日志、事件日志、告警日志和安全日志。

## 注意事项

若日志记录的命令中含有“+++”和“--- END”等MML输出信息开始和结束标志，可能导致此命令查询的日志信息不全。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STARTTIME | 开始时间 | 可选必选说明：可选参数<br>参数含义：查询开始时间。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。<br>默认值：无 |
| ENDTIME | 结束时间 | 可选必选说明：可选参数<br>参数含义：查询结束时间。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。<br>默认值：无 |
| LEVELENUM | 日志级别 | 可选必选说明：可选参数<br>参数含义：日志级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- emergencies：日志级别为紧急。<br>- alert：日志级别为警报。<br>- critical：日志级别为严重。<br>- error：日志级别为错误。<br>- warning：日志级别为警告。<br>- notification：日志级别为通知。<br>- informational：日志级别为提示。<br>- debugging：日志级别为调试。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOGBUFFER]] · Logbuffer中的数据（LOGBUFFER）

## 使用实例

- 不指定参数显示日志缓冲区中的数据：
  ```
  DSP LOGBUFFER:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  日志级别         日志内容

  通知             Sep  3 2017 17:31:13 "HUAWEI" %%01SSH/5/SSH_USER_LOGIN(s):CID=0x80930038;SSH用户成功地登录。（服务类型＝stelnet，用户名＝omuser，IP地址＝192.168.7.5，VPN实例索引＝__mpp_vpn_outer__）
  通知             Sep  3 2017 17:31:42 "HUAWEI" %%01SSH/5/SSH_USER_LOGIN(s):CID=0x80930038;SSH用户成功地登录。（服务类型＝stelnet，用户名＝omuser，IP地址＝192.168.7.5，VPN实例索引＝__mpp_vpn_outer__）                                                                                                                                                                                                                                                                    
  (结果个数 = 2)
  ---    END
  ```
- 指定级别（ notification）显示日志缓冲区中的数据：
  ```
  DSP LOGBUFFER: LEVELENUM=notification
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  日志级别         日志内容
                                                                                                                                                                                                                                                                                                                                                                      
  通知             Sep  3 2017 17:31:13 "HUAWEI" %%01SSH/5/SSH_USER_LOGIN(s):CID=0x80930038;SSH用户成功地登录。（服务类型＝stelnet，用户名＝omuser，IP地址＝192.168.7.5，VPN实例索引＝__mpp_vpn_outer__）
  通知             Sep  3 2017 17:31:42 "HUAWEI" %%01SSH/5/SSH_USER_LOGIN(s):CID=0x80930038;SSH用户成功地登录。（服务类型＝stelnet，用户名＝omuser，IP地址＝192.168.7.5，VPN实例索引＝__mpp_vpn_outer__）
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-LOGBUFFER.md`
