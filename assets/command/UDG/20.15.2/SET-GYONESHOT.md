---
id: UDG@20.15.2@MMLCommand@SET GYONESHOT
type: MMLCommand
name: SET GYONESHOT（设置Gy一次重定向参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GYONESHOT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- Gy接口一次重定向控制
- Gy接口一次重定向
status: active
---

# SET GYONESHOT（设置Gy一次重定向参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置Gy接口一次重定向的URL白名单列表，并配置是否包含重定向携带信息。匹配上该白名单的报文将被重定向到OCS下发的URL。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 若命令配置为重定向URL中可包含重定向携带信息。而如果重定向携带信息包含原始请求URL，名称为reqUrlName，携带用户的MSISDN，名称为msisdnName，携带用户的IMSI，名称为imsiName，携带用户的IMEI，名称为imeiName，携带用户的IP信息，名称为msipName，则URL重定向中报文内容为： Location: http://www.example.com/?reqUrlName=http://10.13.4.3/6.htm&msisdnName=18612345678&imsiName=123456789012345&imeiName=123456789012346&msipName=10.110.220.97 上面报文中的内容原始请求的URL为10.13.4.3/6.htm，用户的MSISDN为18612345678，用户的IMSI为123456789012345，用户的IMEI为123456789012346，用户的MSIP为10.110.220.97。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REDIRAGETIME |
| --- | --- |
| 初始值 | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTFLTNAME | 扩展过滤器名字 | 可选必选说明：可选参数<br>参数含义：该参数用于设置一次重定向动作的ExtendedFilter名称。在执行一次重定向动作时，对于匹配到ExtendedFilter的报文执行重定向动作。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数需要使用ADD EXTENDEDFILTER提前配置生成后才能使用。 |
| REDIRAGETIME | 重定向完成时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置一次重定向完成时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～600。<br>默认值：无<br>配置原则：该参数未使用，时间使用srvcommpara中参数，配置后不生效。 |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD REDIRAPPENDINFO命令配置生成。<br>- 设置的AppendInfoName必须是系统已经存在的名称。 |

## 操作的配置对象

- [Gy一次重定向参数（GYONESHOT）](configobject/UDG/20.15.2/GYONESHOT.md)

## 关联任务

- [0-00024](task/UDG/20.15.2/0-00024.md)

## 使用实例

假设运营商需要配置一个一次重定向的URL白名单列表，按如下命令配置：

```
SET GYONESHOT: EXTFLTNAME="test", APPENDINFONAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置Gy一次重定向参数（SET-GYONESHOT）_82837567.md`
