---
id: UNC@20.15.2@MMLCommand@LST MVNOFUN
type: MMLCommand
name: LST MVNOFUN（查询MVNO功能配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MVNOFUN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO功能配置表
status: active
---

# LST MVNOFUN（查询MVNO功能配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询MVNO的功能配置信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询此MVNO用户的功能配置。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [MVNO功能配置信息（MVNOFUN）](configobject/UNC/20.15.2/MVNOFUN.md)

## 使用实例

查询所有的MVNO的功能：

LST MVNOFUN:;

```
%%LST MVNOFUN:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
         MVNO标识  =  2
   是否支持短消息  =  是
      是否支持LCS  =  是
是否支持SNDCP压缩  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MVNO功能配置信息(LST-MVNOFUN)_72225741.md`
