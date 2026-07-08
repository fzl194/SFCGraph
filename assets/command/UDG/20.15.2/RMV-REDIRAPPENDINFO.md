---
id: UDG@20.15.2@MMLCommand@RMV REDIRAPPENDINFO
type: MMLCommand
name: RMV REDIRAPPENDINFO（删除重定向携带信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: REDIRAPPENDINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 重定向公共参数管理
- 重定向携带信息
status: active
---

# RMV REDIRAPPENDINFO（删除重定向携带信息）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商删除已经配置的重定向携带信息。

## 注意事项

- 该命令执行后立即生效。
- 输入APPENDINFONAME删除指定记录，不输入APPENDINFONAME删除所有记录。
- 如果被Redirect、FuiEnrichment、GyOneshot、SmartHttpRedir、IPFarmServer引用则不允许删除，需先解除绑定，才能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/REDIRAPPENDINFO]] · 重定向携带信息（REDIRAPPENDINFO）

## 使用实例

运营商希望删除名为“testredirappendinfo”的重定向携带信息：

```
RMV REDIRAPPENDINFO: APPENDINFONAME="testredirappendinfo";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-REDIRAPPENDINFO.md`
