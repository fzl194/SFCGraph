---
id: UDG@20.15.2@MMLCommand@LST NGLANATTR
type: MMLCommand
name: LST NGLANATTR（查询5G LAN属性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGLANATTR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN属性配置
status: active
---

# LST NGLANATTR（查询5G LAN属性配置）

## 功能

**适用NF：UPF**

该命令用于查询指定5G LAN组的属性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G LAN属性配置（NGLANATTR）](configobject/UDG/20.15.2/NGLANATTR.md)

## 使用实例

查询指定5G LAN组总的MAC地址超限个数：

```
LST NGLANATTR: VNINSTANCE="a0000001-460-003-50";
```

```

%%LST NGLANATTR: VNINSTANCE="a0000001-460-003-50";%%
RETCODE = 0 操作成功

结果如下
--------
     5G LAN组名称  =  a0000001-460-003-50
支持的总MAC地址数  =  2000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询5G-LAN属性配置（LST-NGLANATTR）_83372126.md`
