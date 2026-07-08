---
id: UDG@20.15.2@MMLCommand@SET FABRICINSWITCH
type: MMLCommand
name: SET FABRICINSWITCH（设置Fabric-In功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FABRICINSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET FABRICINSWITCH（设置Fabric-In功能开关）

## 功能

该命令用于设置Fabric-In功能开关。Fabric-In对应是内置FullMesh卡，内置FullMesh卡负责框内流量交换。

## 注意事项

该命令本版本不再支持生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | 功能是否开启 | 可选必选说明：必选参数<br>参数含义：该参数表示是否开启和关闭Fabric-In功能。数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”<br>默认值：TRUE |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FABRICINSWITCH]] · Fabric-In功能开关（FABRICINSWITCH）

## 使用实例

- 设置Fabric-In功能开启：
  ```
  %%SET FABRICINSWITCH: ENABLE=TRUE;%%
  RETCODE = 0  操作成功

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-FABRICINSWITCH.md`
