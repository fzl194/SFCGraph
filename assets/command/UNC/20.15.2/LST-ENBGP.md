---
id: UNC@20.15.2@MMLCommand@LST ENBGP
type: MMLCommand
name: LST ENBGP（查询eNodeB群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ENBGP
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB群组管理
status: active
---

# LST ENBGP（查询eNodeB群组）

## 功能

**适用网元：MME**

此命令用于查询eNodeB群组记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>数据来源：本端规划<br>取值范围：1~2048<br>默认值：无 |
| TYPE | 类型 | 可选必选说明：可选参数<br>参数含义：用于指定该eNodeB群组的类型。<br>数据来源：整网规划<br>取值范围：<br>- “ENTRY(入口)”<br>- “INSIDE(内部)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBGP]] · eNodeB群组（ENBGP）

## 使用实例

查询所有eNodeB群组记录：

LST ENBGP:;

```
%%LST ENBGP:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
eNodeB群组标识  =  1
          类型  =  入口
驻留时长（min） =  NULL
      接入次数  =  0
eNodeB群组名称  =  highspeed_usercheck_entry
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ENBGP.md`
