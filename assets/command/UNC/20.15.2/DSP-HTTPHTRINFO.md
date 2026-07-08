---
id: UNC@20.15.2@MMLCommand@DSP HTTPHTRINFO
type: MMLCommand
name: DSP HTTPHTRINFO（显示HTR信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTTPHTRINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP HTR流控管理
- HTTP HTR流控状态管理
status: active
---

# DSP HTTPHTRINFO（显示HTR信息）

## 功能

该命令用于显示特定局向的HTR信息，显示信息包含HTR流控阈值和流控状态等HTR流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCIDX | 局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于显示局向索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTR信息（HTTPHTRINFO）](configobject/UNC/20.15.2/HTTPHTRINFO.md)

## 使用实例

查询局向1的HTR信息，可以执行下面的命令。

```
%%DSP HTTPHTRINFO: OFCIDX=1;%%
RETCODE = 0  操作成功

结果如下
--------
POD名称                   进程标识  状态  初始放通阈值  最小安全边界  最大安全边界  发送请求总数  接收对端过载响应总数  等待对端响应超时总数  请求流控总数  周期内发送请求数  周期内失败率     周期内接收对端过载响应数  周期内等待对端响应超时数  周期内流控请求数  

sbim-pod-87bb9967f-42gjc  17        正常  0             0             0             0             0                     0                     0             0/0/0/0/0/        0%/0%/0%/0%/0%/  0/0/0/0/0/                0/0/0/0/0/                0/0/0/0/0/        
sbim-pod-87bb9967f-42gjc  18        正常  0             0             0             0             0                     0                     0             0/0/0/0/0/        0%/0%/0%/0%/0%/  0/0/0/0/0/                0/0/0/0/0/                0/0/0/0/0/        
sbim-pod-87bb9967f-42gjc  19        正常  0             0             0             0             0                     0                     0             0/0/0/0/0/        0%/0%/0%/0%/0%/  0/0/0/0/0/                0/0/0/0/0/                0/0/0/0/0/        
sbim-pod-87bb9967f-42gjc  20        正常  0             0             0             0             0                     0                     0             0/0/0/0/0/        0%/0%/0%/0%/0%/  0/0/0/0/0/                0/0/0/0/0/                0/0/0/0/0/            
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示HTR信息（DSP-HTTPHTRINFO）_52280610.md`
