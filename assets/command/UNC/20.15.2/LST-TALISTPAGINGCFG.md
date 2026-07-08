---
id: UNC@20.15.2@MMLCommand@LST TALISTPAGINGCFG
type: MMLCommand
name: LST TALISTPAGINGCFG（查询TALIST寻呼不重发TAC区间）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TALISTPAGINGCFG
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- S1寻呼TALIST寻呼管理
status: active
---

# LST TALISTPAGINGCFG（查询TALIST寻呼不重发TAC区间）

## 功能

**适用网元：MME**

该命令用于查询TALIST寻呼不重发TAC区间。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0x0000~0xFFFF，输入时可以不输入0x前缀。<br>默认值： 无 |

## 操作的配置对象

- [TALIST寻呼不重发TAC区间（TALISTPAGINGCFG）](configobject/UNC/20.15.2/TALISTPAGINGCFG.md)

## 使用实例

查询TAC跟踪区间：

LST TALISTPAGINGCFG:;

```
%%LST TALISTPAGINGCFG:;%%
RETCODE = 0  操作成功

输出结果如下
------------
          跟踪区域码  =  0x12
      跟踪区域码范围  =  0x34
    语音寻呼重传开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TALIST寻呼不重发TAC区间(LST-TALISTPAGINGCFG)_26306198.md`
