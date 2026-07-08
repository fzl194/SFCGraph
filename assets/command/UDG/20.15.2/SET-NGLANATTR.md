---
id: UDG@20.15.2@MMLCommand@SET NGLANATTR
type: MMLCommand
name: SET NGLANATTR（设置5G LAN属性配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NGLANATTR
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN属性配置
status: active
---

# SET NGLANATTR（设置5G LAN属性配置）

## 功能

**适用NF：UPF**

该命令用于设置指定5G LAN组的相关属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。<br>默认值：无<br>配置原则：无 |
| TOTALMACNUM | 支持的总MAC地址数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置5G LAN组支持学习的总的MAC地址数。<br>数据来源：本端规划<br>取值范围：当5GLAN组的PDN类型为ETH时，只允许配置1024到8000；当5GLAN组的PDN类型为IP时，只允许配置0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G LAN属性配置（NGLANATTR）](configobject/UDG/20.15.2/NGLANATTR.md)

## 使用实例

设置指定5G LAN组总的MAC地址超限个数：

```
SET NGLANATTR: VNINSTANCE="A0000001-460-003-30", TOTALMACNUM=1024;

%%SET NGLANATTR: VNINSTANCE="a0000001-460-003-50", TOTALMACNUM=2000;%%
RETCODE = 0 操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置5G-LAN属性配置（SET-NGLANATTR）_83132818.md`
