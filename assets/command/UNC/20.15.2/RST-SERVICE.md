---
id: UNC@20.15.2@MMLCommand@RST SERVICE
type: MMLCommand
name: RST SERVICE（复位业务）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: SERVICE
command_category: 动作类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 业务管理
status: active
---

# RST SERVICE（复位业务）

## 功能

![](复位业务（RST SERVICE）_51174329.assets/notice_3.0-zh-cn_2.png)

复位业务属于危险操作。如果参数配置有误，重启后会导致业务故障。建议不要在业务繁忙时进行此项操作。

**适用NF：NCG**

该命令用于将UNC上的所有业务重新启动。系统会去激活所有的业务进程。

在更改了不能动态生效的参数后，需要复位业务，使参数生效。

## 注意事项

- 复位业务属于危险操作。如果参数配置有误，重启后会导致业务故障。建议不要在业务繁忙时进行此项操作。
- 进行复位时会停止接收处理话单，复位时间一般小于1分钟（不超过5分钟）。
- 复位之后可以使用[**DSP SERVICE**](显示业务状态（DSP SERVICE）_51174328.md)查询业务进程状态，查看重启后业务进程状态是否正常。
- 系统初始化配置完成以后，执行[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)命令使配置生效。
- 系统正常运行的过程中，修改NCG配置需要执行[**RST SERVICE**](复位业务（RST SERVICE）_51174329.md)使修改生效。
- 系统正常运行的过程中，如果新增了RU，需要执行[**RST RU**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/重启资源单元（RST RU）_59103467.md)命令复位新增RU使配置生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SERVICE]] · 复位业务（SERVICE）

## 使用实例

重启所有的业务：

```
RST SERVICE:;
RETCODE = 0  操作成功。

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位业务（RST-SERVICE）_51174329.md`
