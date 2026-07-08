---
id: UNC@20.15.2@MMLCommand@DSP FEATUREOPRHIST
type: MMLCommand
name: DSP FEATUREOPRHIST（查询特性上下线历史）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FEATUREOPRHIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 服务部署管理
status: active
---

# DSP FEATUREOPRHIST（查询特性上下线历史）

## 功能

查询特性上下线历史。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [特性上下线历史（FEATUREOPRHIST）](configobject/UNC/20.15.2/FEATUREOPRHIST.md)

## 使用实例

DSP FEATUREOPRHIST:;

```
%%DSP FEATUREOPRHIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                          操作类型  =  特性上线
记录操作对象信息(Feature和Pod信息)  =  usnom-pod:1,usn-pod:1
                      处理开始时间  =  20191216-14:17:35
                      处理结束时间  =  20191216-14:17:35
                          结果说明  =  NULL
                          处理结果  =  处理成功
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询特性上下线历史（DSP-FEATUREOPRHIST）_14567237.md`
