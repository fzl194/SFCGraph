---
id: UNC@20.15.2@MMLCommand@LST VNODE
type: MMLCommand
name: LST VNODE（查询虚拟节点信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VNODE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 应用编排管理
status: active
---

# LST VNODE（查询虚拟节点信息）

## 功能

该命令用于查询虚拟节点信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNFCNAME | VNFC实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VNFP或VNFC实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNODE]] · 虚拟节点信息（VNODE）

## 使用实例

查询虚拟节点信息：

```
LST VNODE:VNFCNAME="kk";
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
                虚拟节点名称   = VNODE_VNRS_VNFC_OMU_0001 
            虚拟节点类型名称   = VNODE_VNRS_VNFC_OMU
      虚拟节点亲和组实例名称   = VNODEG_XXX_OMU_001
                VNFC实例名称   = kk
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VNODE.md`
