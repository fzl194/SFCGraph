---
id: UDG@20.15.2@MMLCommand@LOD TETHERDB
type: MMLCommand
name: LOD TETHERDB（加载Tethering检测特征库）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: TETHERDB
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering检测特征库
status: active
---

# LOD TETHERDB（加载Tethering检测特征库）

## 功能

**适用NF：PGW-U、UPF**

该命令用于加载/升级Tethering检测特征库。

## 注意事项

- 该命令执行后立即生效。
- 此命令的生效范围为整机。
- 新增Tethering数据库可以通过网管/MAE的“网元文件传输”功能或者OM Portal的“文件传输”功能进行库文件上传。
- 数据库加载或更新需要一段时间，如果在执行完毕之前重新执行本命令，系统会提示错误。
- 加载或者卸载命令两次执行间隔不能小于10s。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VERSION | Tethering检测特征库版本号 | 可选必选说明：必选参数<br>参数含义：该参数用来显示Tethering Database 的版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～21。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TETHERDB]] · Tethering检测特征库（TETHERDB）

## 使用实例

假如运营商需要加载或升级Tethering检测特征库：

```
LOD TETHERDB: VERSION="9001.01.0000.0000.115";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LOD-TETHERDB.md`
