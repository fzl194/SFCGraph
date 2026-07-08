---
id: UNC@20.15.2@MMLCommand@LST IUDETACH
type: MMLCommand
name: LST IUDETACH（查询Iu分离非活动用户参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUDETACH
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 分离非活动用户
- Iu模式分离非活动用户参数
status: active
---

# LST IUDETACH（查询Iu分离非活动用户参数）

## 功能

**适用网元：SGSN**

此命令用于查询3G分离非活动用户配置参数。当用户通过附着或路由区更新流程接入到本SGSN后，如果在指定时长(大于 “非活动用户分离定时器(分)” 时长)没有PDP（Packet Data Protocol）激活，则认为该用户为非活动用户对用户进行分离操作；当系统将用户判断为非活动用户进行分离后，如果用户马上重新附着且与上次分离的时间间隔不超过配置的 “永久在线识别定时器长(秒)” 时长， 则该用户被定义为永久在线用户，后续系统不会对该用户进行分离非活动用户操作。SGSN发起分离非活动用户的流程，可以释放这些用户的空闲资源，以支持更多的用户。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IUDETACH]] · Iu分离非活动用户参数（IUDETACH）

## 使用实例

查询3G分离非活动用户配置参数：

LST IUDETACH:;

```
%%LST IUDETACH:;%%
RETCODE = 0  操作成功。

3G分离非活动用户配置表
----------------------
                         非活动用户分离  =  否
               非活动用户分离定时器(分)  =  360
是否在Follow-on时启用分离非活动用户功能  =  否
                              保留参数1  =  否
                              保留参数2  =  0
                              保留参数3  =  0
               永久在线识别定时器长(秒)  =  60
                           永久在线识别  =  否
           是否在分离响应超时后分离用户  =  是
                           分离用户方式  =  IMPLICITLY
                              保留参数4  =  IMPLICITLY
                              保留参数5  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IUDETACH.md`
