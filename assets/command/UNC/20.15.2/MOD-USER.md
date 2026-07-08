---
id: UNC@20.15.2@MMLCommand@MOD USER
type: MMLCommand
name: MOD USER（修改用户操作权限）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: USER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 用户管理
status: active
---

# MOD USER（修改用户操作权限）

## 功能

![](修改用户操作权限(MOD USER)_06404642.assets/notice_3.0-zh-cn_2.png)

该操作将修改用户操作权限，同时注销该用户所有在线会话。

编辑用户对应的角色。

- 角色：特定的一些操作权限组成的权限集合。可以通过OM Portal的“ 安全 > 用户管理 > 角色 ”创建和查询。
- 账号策略：对于账号的一些特定要求，可以通过OM Portal的“ 安全 > 安全策略 ”查询。
- 密码策略：对于密码的一些特定要求，可以通过OM Portal的“ 安全 > 安全策略 ”查询。
- 默认用户：系统缺省已配置的用户，可以通过OM Portal的“ 安全 > 用户管理 ”查询。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| USRNAME | 用户名称 | 可选必选说明：必选参数。<br>参数含义：用户名称，可在OM Portal的“安全 > 用户管理”查询。<br>取值范围：长度不超过32个字符。<br>默认值：无。<br>配置原则：无。 |
| OPTYPE | 操作类型 | 可选必选说明：必选参数。<br>参数含义：操作类型。<br>取值范围：<br>- ADD(新增)：为用户新增一个角色。<br>- DEL(删除)：为用户删除一个角色。<br>默认值：无。<br>配置原则：无。 |
| ROLENAME | 角色名称 | 可选必选说明：必选参数。<br>参数含义：角色是特定操作权限的集合。为用户添加角色，即是将角色包括的权限赋予用户。<br>取值范围：长度不超过64个字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USER]] · 用户锁定状态（USER）

## 使用实例

修改用户test01操作权限为Operators角色所含权限：

```
%%MOD USER: USRNAME="test01", OPTYPE=ADD, ROLENAME="Operators";%% 
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改用户操作权限(MOD-USER)_06404642.md`
