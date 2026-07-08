---
id: UNC@20.15.2@MMLCommand@LST MVNONET
type: MMLCommand
name: LST MVNONET（查询MVNO网络配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MVNONET
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO网络标识配置表
status: active
---

# LST MVNONET（查询MVNO网络配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于用户查询MVNO网络配置信息。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOMCC | MVNO移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动国家代码。<br>取值范围：3位十进制数<br>默认值：无 |
| MVNOMNC | MVNO移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动网号。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户除了MCC和MNC外的IMSI的字段。<br>取值范围：长度不超过10的十进制数字<br>默认值：无 |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定根据MVNO标识查询这个MVNO的网络配置。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MVNONET]] · MVNO网络配置信息（MVNONET）

## 使用实例

查询所有的MVNO的网络资源配置：

LST MVNONET:;

```
%%LST MVNONET:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
       MVNO移动国家码  =  460
         MVNO移动网号  =  00
             匹配IMSI  =  111
           MVNO国家码  =  860
             MVNO标识  =  2
 是否允许紧急呼叫业务  =  允许
     紧急号码下发开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MVNONET.md`
