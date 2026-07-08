---
id: UNC@20.15.2@MMLCommand@LST SMFSELUDM
type: MMLCommand
name: LST SMFSELUDM（查询SMF选择UDM策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFSELUDM
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- NF发现和选择管理
- UDM选择策略管理
status: active
---

# LST SMFSELUDM（查询SMF选择UDM策略）

## 功能

**适用NF：SMF**

该命令用于查询UDM的选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMF选择UDM策略（SMFSELUDM）](configobject/UNC/20.15.2/SMFSELUDM.md)

## 使用实例

查询当前配置的UDM选择策略，执行如下命令：

```
%%LST SMFSELUDM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
               用户范围  =  Foreign Subscriber
           是否使用GPSI  =  YES
       是否使用网络切片  =  NO
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF选择UDM策略（LST-SMFSELUDM）_48290737.md`
