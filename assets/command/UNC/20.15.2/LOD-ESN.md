---
id: UNC@20.15.2@MMLCommand@LOD ESN
type: MMLCommand
name: LOD ESN（加载设备序列号）
nf: UNC
version: 20.15.2
verb: LOD
object_keyword: ESN
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# LOD ESN（加载设备序列号）

## 功能

该命令用于自动化部署网元场景中为网元加载用户指定的设备序列号（ESN）。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行后立即生效。
- 该命令只能在自动化部署新建网元场景中使用。非自动化部署场景下执行该命令会导致系统异常。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESN | 设备序列号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定当前网元的设备序列号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>在自动化部署新建网元场景中，从CloudDesign工具中获得设备序列号。 |
| VERIFICATION | 验证码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与加载设备序列号配套的验证码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>在自动化部署新建网元场景中，从CloudDesign工具中获得设备序列号配套的验证码。 |

## 操作的配置对象

- [设备序列号（ESN）](configobject/UNC/20.15.2/ESN.md)

## 使用实例

加载用户指定设备序列号，执行以下命令：

```
%%LOD ESN: ESN="RA201810182045026CC33CB8F85394264C06", VERIFICATION="55D33CC694AE57748156425A6ADEFFFC17F9F20811EB8445ADAF79150BA21527";%%
RETCODE = 0 操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/加载设备序列号（LOD-ESN）_09653138.md`
