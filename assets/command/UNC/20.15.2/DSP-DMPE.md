---
id: UNC@20.15.2@MMLCommand@DSP DMPE
type: MMLCommand
name: DSP DMPE（显示Diameter对端实体）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DMPE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter对端实体
status: active
---

# DSP DMPE（显示Diameter对端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于查看Diameter对端实体状态。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIDX | 对端实体索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter对端实体索引。<br>取值范围：0～639<br>默认值：无<br>说明：如果不输入，表示查询所有与系统相连的Diameter对等端状态。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMPE]] · Diameter对端实体（DMPE）

## 使用实例

查询Diameter对等端实体状态。

%DSP DMPE:;

```
%%DSP DMPE:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 对端实体索引  对端实体名  实体状态

 0             huaweiHSS1  正常    
 1             huaweiHSS2  正常    
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DMPE.md`
