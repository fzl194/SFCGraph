---
id: UDG@20.15.2@MMLCommand@LST CERTSCENE
type: MMLCommand
name: LST CERTSCENE（查询证书场景）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CERTSCENE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 公钥基础设施
- PKI场景
status: active
---

# LST CERTSCENE（查询证书场景）

## 功能

该命令用于查询证书场景。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENENAME | 场景名称 | 可选必选说明：可选参数<br>参数含义：场景名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~192。不区分大小写，最多允许一个空格，不支持中文字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CERTSCENE]] · 证书场景描述（CERTSCENE）

## 使用实例

查询场景名为“DeviceA”的证书场景：

```
%%LST CERTSCENE: SCENENAME="DeviceA";%%
RETCODE = 0  操作成功

结果如下
--------
    场景名称  =  devicea
    场景类型  =  本地证书
场景英文描述  =  devicea
场景中文描述  =  devicea
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询证书场景（LST-CERTSCENE）_26150753.md`
