---
id: UDG@20.15.2@MMLCommand@DSP MKUNSYNCTARGET
type: MMLCommand
name: DSP MKUNSYNCTARGET（查询主密钥未同步的对象）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MKUNSYNCTARGET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 主密钥管理
status: active
---

# DSP MKUNSYNCTARGET（查询主密钥未同步的对象）

## 功能

该命令用于查询主密钥未同步的对象。当更新密钥失败时，可使用该命令查询主密钥未同步的资源。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MKUNSYNCTARGET]] · 主密钥未同步的对象（MKUNSYNCTARGET）

## 使用实例

查询主密钥未同步的对象：

```
DSP MKUNSYNCTARGET:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------------
RU名称                 
VNODE_CSLB_VNFC_OMU_0001
VNODE_CSLB_VNFC_OMU_0002
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MKUNSYNCTARGET.md`
