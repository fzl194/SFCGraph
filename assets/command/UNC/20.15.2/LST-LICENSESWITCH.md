---
id: UNC@20.15.2@MMLCommand@LST LICENSESWITCH
type: MMLCommand
name: LST LICENSESWITCH（查询License配置项开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LICENSESWITCH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# LST LICENSESWITCH（查询License配置项开关）

## 功能

该命令用于查看License项的名称以及License项的开关配置情况。

## 注意事项

- 该命令执行后立即生效。
- 当license文件未激活时，查询结果为空，激活后只能查询已购买且支持配置开关的license项。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LICITEM | License项 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要开通的License项。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [License配置项开关（LICENSESWITCH）](configobject/UNC/20.15.2/LICENSESWITCH.md)

## 使用实例

查询License项“LKV2INLIAM01”的配置开关：

```
%%LST LICENSESWITCH: LICITEM="LKV2INLIAM01";%%
RETCODE = 0  操作成功

操作结果如下
------------
  License项  =  LKV2INLIAM01
License名称  =  IPv6 Networking on Logic Interface-UAM
       开关  =  开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询License配置项开关（LST-LICENSESWITCH）_09651570.md`
