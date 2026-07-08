---
id: UNC@20.15.2@MMLCommand@LST IUAUTHCIPH
type: MMLCommand
name: LST IUAUTHCIPH（查询Iu模式用户安全参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IUAUTHCIPH
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Iu模式用户安全参数
status: active
---

# LST IUAUTHCIPH（查询Iu模式用户安全参数）

## 功能

**适用网元：SGSN**

该命令用于查询3G鉴权加密信息表记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “SPECIAL_USER（指定用户）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制数字<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [Iu模式用户安全参数（IUAUTHCIPH）](configobject/UNC/20.15.2/IUAUTHCIPH.md)

## 使用实例

以SUBRANGE为条件查询所有UTRAN用户鉴权加密配置：

LST IUAUTHCIPH:;

```
%%LST IUAUTHCIPH:;%%
RETCODE = 0  操作成功。

3G用户鉴权配置表
----------------
                                用户范围  =  所有用户
                                 IMSI前缀 =  NULL
                                安全策略  =  鉴权并保护
                                鉴权事件  =  MS发起的服务请求 & INTER位置更新 & 使用PTMSI的附着 & 使用IMSI的附着 & PTMSI签名不匹配 & 重分配后的INTER 位置更新 
                            鉴权事件上限  =  1
           是否支持附着流程的二次鉴权功能 =  否
       是否支持路由更新流程的二次鉴权功能 =  否
	           是否支持V2取鉴权集功能 =  否
                                 鉴权周期 =  24
                               鉴权集数量 =  5
                          是否预取鉴权集  =  是
                       预先取鉴权集门限值 =  0
                                 重复鉴权 =  否
                   用户鉴权失败次数临界值 =  3
                                 加密算法 =  UEA1 & UEA2 & NO_ENCRYPTION
                              完整性算法  =  UIA1 & UIA2
                            强制身份识别  =  否
(结果个数 = 1)
--    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Iu模式用户安全参数(LST-IUAUTHCIPH)_26145648.md`
