---
id: UNC@20.15.2@MMLCommand@LST UEUSGTYPEGPMEM
type: MMLCommand
name: LST UEUSGTYPEGPMEM（查询UE USAGE TYPE群组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UEUSGTYPEGPMEM
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- UE USAGE TYPE群组成员管理
status: active
---

# LST UEUSGTYPEGPMEM（查询UE USAGE TYPE群组成员）

## 功能

**适用网元：MME**

该命令用于查询UE USAGE TYPE群组成员。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无 |
| BGNUEUSGTYPE | 起始UE USAGE TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE的起始值。<br>数据来源：本端规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEUSGTYPEGPMEM]] · UE USAGE TYPE群组成员（UEUSGTYPEGPMEM）

## 使用实例

查询 “UE USAGE TYPE群组标识” 为 “1” 的UE USAGE TYPE群组成员记录：

LST UEUSGTYPEGPMEM: UEUSGTYPEGPID=1;

```
%%LST UEUSGTYPEGPMEM: UEUSGTYPEGPID=1;%%
RETCODE = 0  操作成功

操作结果如下
--------------
UE USAGE TYPE群组标识  =  1
    起始UE USAGE TYPE  =  100
    终止UE USAGE TYPE  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UEUSGTYPEGPMEM.md`
