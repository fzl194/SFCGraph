---
id: UNC@20.15.2@MMLCommand@LST IPAREAAPN
type: MMLCommand
name: LST IPAREAAPN（查询IP区域APN网络标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPAREAAPN
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
- 移动性管理
- 基于位置分配IP地址管理
- 基于位置分配IP地址APN信息配置
status: active
---

# LST IPAREAAPN（查询IP区域APN网络标识）

## 功能

**适用网元：SGSN、MME**

该命令用于查询为“基于位置的IP地址重分配”功能配置的APN网络标识信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定支持“基于位置的IP地址重分配”功能的APN网络标识。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾<br>- “*”表示通配符，如果APN网络标识为“*”，表示所有APN网络标识都支持“基于位置的IP地址重分配”功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPAREAAPN]] · IP区域APN网络标识（IPAREAAPN）

## 使用实例

查询系统中“基于位置的IP地址重分配”功能配置的APN网络标识信息：

LST IPAREAAPN:;

```
%%LST IPAREAAPN:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
    APN网络标识  =  HUAWEI.COM 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IP区域APN网络标识(LST-IPAREAAPN)_72225285.md`
